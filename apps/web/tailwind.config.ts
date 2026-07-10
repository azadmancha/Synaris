import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          950: "#0f172a",
          900: "#111827",
          700: "#1d4ed8",
          500: "#2563eb",
          300: "#93c5fd",
        },
      },
    },
  },
  plugins: [],
};

export default config;
