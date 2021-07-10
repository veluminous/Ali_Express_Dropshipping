from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..database import crud, schemas, models
from ..dependencies import get_db
from ..zapiex.zapiex import zapiex_apis

router = APIRouter(prefix="/products", tags=["products"])

""" HW July 3rd
1. When SearchText is stored but ProductList isn't, return [] -> Please making sure both SearchText and ProductList are stored 
2. Search API analysis
3. crud, model, router setting for ProductDetail API
4. Schemas setting for search, ProductDetail, SearchText
"""


@router.post("/", response_model=schemas.ProductList)
async def search_items_by_text(text: str, page: int, db: Session = Depends(get_db)):
    try:
        search_text = crud.get_search_text_and_page(db, text=text, page=page)
        # 이미 검색한 기록이 있으면 db에서 꺼내 보여줌
        if search_text:
            return search_text.product_list[0]
        search_info = zapiex_apis.search_products(text, page)  # Zapiex API 호출
        if search_info["statusCode"] == 200:
            search_text = crud.create_search_text(
                db=db, text=text, page=page
            )  # search_text 테이블에 저장
            information = search_info["data"]
            return crud.create_searched_products(
                db=db, information=information, search_text_id=search_text.id
            )
        else:
            raise HTTPException(status_code=400, detail={"error_code": 1})
    except Exception:
        # raise HTTPException(detail=e, status_code=400)
        # print(e)
        raise


# @router.post("/{product_id}", response_model=schemas.ProductDetail)
@router.post("/{product_id}")
def create_details(product_id: str, db: Session = Depends(get_db)):
    try:
        db_detail = crud.get_product_detail(db, product_id=product_id)
        if db_detail:
            return db_detail
        product_info = zapiex_apis.get_product(product_id)
        if product_info["statusCode"] == 200:
            information = product_info["data"]
            if information["status"] == "active":
                return crud.create_product_details(db=db, information=information)
            else:
                return information
        else:
            raise HTTPException(
                status_code=product_info["statusCode"], detail=product_info["errorMessage"]
            )
    except Exception:
        raise