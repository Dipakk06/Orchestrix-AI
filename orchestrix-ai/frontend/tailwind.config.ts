import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        surface: '#101729',
      },
      backgroundImage: {
        mesh: 'radial-gradient(circle at 20% 20%, rgba(98,0,234,0.3), transparent 30%), radial-gradient(circle at 80% 40%, rgba(33,150,243,0.3), transparent 35%)',
      },
    },
  },
  plugins: [],
}

export default config
