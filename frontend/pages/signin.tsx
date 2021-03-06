import Link from 'next/link'
import Head from 'next/head'
import { useRouter } from 'next/router'
import Layout from '../src/components/layout'

import { useState } from "react";
import { useEffect } from 'react'
import { useCookies } from "react-cookie"
import axios from 'axios';
import FormData from 'form-data';

export default function Signin() {
  const [cookies, setCookie, removeCookie] = useCookies(["access_token"]);
  const router = useRouter();
  
  let access_token = cookies.access_token;
  useEffect(() => {
    // authentication of JWT token
    if (!access_token) {
      return;
    }
    const verifyTokenForReturl = async () => { 
      try{
        let retUrl = router.query.retUrl;
        const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/aaa/token`, {
          headers: {
              Authorization: `bearer ${access_token}`
          }
        }); 
        if (response.data.valid && retUrl && typeof retUrl === 'string') {
          router.push(retUrl);
        } else if (response.data.valid) {
          router.push('/products');
        }
      } catch (error) {
        // Delete access token cookie
        removeCookie('access_token');
      }
    }
    verifyTokenForReturl();
  })

  const [ email, setEmail ] = useState("");
  const [ password, setPassword ] = useState("");
  const [ isInvalid, setIsInvalid ] = useState(false);

  const handleEmailChange = ({ target: { value } }) => setEmail(value);
  const handlePasswordChange = ({ target: { value } }) => setPassword(value);
  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);
    try {
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/aaa/token`,
      formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      if (response.status == 200) {
        const accessToken = response.data.access_token;
        const afterOneDay = new Date();
        afterOneDay.setDate(afterOneDay.getDate() + 1);
        setCookie(
          'access_token', 
          accessToken,
          {
            expires: afterOneDay,
          }
        );
      }
    } catch (error) {
      if (error.response.status === 401) {
        setIsInvalid(true);
      }
      console.log(error);
    }
  };

  return (
    <Layout>
      <Head>
        <title>Signin</title>
      </Head>
      <div className="container d-flex justify-content-center align-items-center" style={{height: "500px"}}>
        <main>
          <form className="row gy-4" style={{width: "400px"}} onSubmit={handleSubmit}>
            <div>
              <input 
                className="form-control form-control-lg"
                name="email" 
                type="email" 
                onChange={handleEmailChange}
                placeholder="Email" />
            </div>
            <div>
              <input 
                className="form-control form-control-lg"
                name="password" 
                type="password" 
                onChange={handlePasswordChange}
                placeholder="Password" />
            </div>
            <div style={{ 
                display: `${(isInvalid && "block") || "none"}`
            }}>
              You entered wrong email or password, Please try to enter the right email and password!
            </div>
            <div className="d-flex justify-content-between">
              <Link href="/signup">
                <a>
                  <div className="btn btn-danger fs-4">
                    Register
                  </div>
                </a>
              </Link>
              <button className="btn btn-danger fs-4" type="submit">Log-in</button>
            </div>
          </form>
        </main>
      </div>
    </Layout>
  )
}