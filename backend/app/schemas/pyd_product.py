from typing import List, Optional
from pydantic import BaseModel


# search text
class SearchText(BaseModel):
    text: str


class SearchTextOutput(SearchText):
    class Config:
        orm_mode = True


# search products
class ProductList(BaseModel):
    id: int
    information: dict
    search_text_id: int

    class Config:
        orm_mode = True


# product details
class ProductDetail(BaseModel):
    id: int
    productUrl: str
    productId: str
    statusId: str
    status: str
    currency: str
    locale: str
    shipTo: str
    title: str
    totalStock: int
    totalOrders: int
    wishlistCount: int
    unitName: str
    unitNamePlural: str
    unitsPerProduct: int
    hasPurchaseLimit: bool
    maxPurchaseLimit: Optional[int]
    processingTimeInDays: int
    productImages: List[str]
    productCategory: dict
    seller: dict
    sellerDetails: dict
    hasSinglePrice: bool
    priceSummary: Optional[dict]
    price: Optional[dict]
    hasAttributes: bool
    attributes: List[dict]
    hasReviewsRatings: bool
    reviewsRatings: dict
    hasProperties: bool
    properties: List[dict]
    hasVariations: bool
    variations: List[dict]
    shipping: dict
    htmlDescription: str

    class Config:
        orm_mode = True
