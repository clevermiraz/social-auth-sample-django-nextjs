"use client";

import { GoogleLogin } from "@react-oauth/google";
import axios from "axios";
import { useEffect, useState } from "react";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;

export default function GoogleLoginButton({ children }) {
    const [isMount, setIsMount] = useState(false);

    useEffect(() => {
        setIsMount(true);
    }, []);

    const handleLoginSuccess = async (response) => {
        try {
            const googleToken = response.credential;

            // Send Google token to the backend for verification
            if (googleToken) {
                const payload = {
                    access_token: `${googleToken}`, // Pass it as access_token in the body
                };

                const config = {
                    headers: {
                        "Content-Type": "application/json", // Ensure the correct content type
                    },
                };

                const response = await axios.post(BACKEND_URL, payload, config);

                return response.data;
            }
        } catch (error) {
            console.error("Error during Google login:", error);
        }
    };

    if (!isMount) return null;

    return (
        <GoogleLogin
            className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
            onSuccess={handleLoginSuccess}
            onError={() => console.error("Google login failed")}
        />
    );
}
