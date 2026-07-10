import NextAuth from "next-auth";
import GoogleProvider from "next-auth/providers/google";

const isProduction = process.env.NODE_ENV === "production";
const cookieDomain = process.env.NEXTAUTH_URL ? new URL(process.env.NEXTAUTH_URL).hostname : "localhost";

const authOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID ?? "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET ?? "",
    }),
  ],
  secret: process.env.AUTH_SECRET ?? "",
  session: {
    strategy: "jwt" as const,
    maxAge: 60 * 60 * 24,
  },
  callbacks: {
    async jwt({ token, user }: { token: any; user?: any }) {
      if (user) {
        return {
          ...token,
          sub: user.email,
          name: user.name,
          picture: user.image,
          email: user.email,
        };
      }
      return token;
    },
    async session({ session, token }: { session: any; token: any }) {
      return {
        ...session,
        user: {
          name: token.name as string,
          email: token.email as string,
          image: token.picture as string,
        },
      };
    },
  },
  cookies: {
    sessionToken: {
      name: "synaris_session_token",
      options: {
        httpOnly: true,
        sameSite: "lax",
        path: "/",
        secure: isProduction,
        domain: cookieDomain,
      },
    },
  },
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };
