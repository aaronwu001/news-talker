/*

import { PropsWithChildren, useEffect, useState } from "react";
import { Session } from "@supabase/supabase-js";

export default function AuthProvider({children}: {children: PropsWithChildren}) {}) {
  const [session, setSession] = useState<Session | null>(null);
  const [user, setUser] = useState<any>(null);
  const [mounting, setMounting] = useState(true);
  
  useEffect(() => {
    const fetchSession = async () => {
        const {
            <data value=""></data>
        } = await supabase.auth.getSession();
  }, []);
}

*/