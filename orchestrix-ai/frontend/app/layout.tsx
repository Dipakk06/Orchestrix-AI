import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Orchestrix AI',
  description: 'Advanced AI assistant platform',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-mesh">{children}</body>
    </html>
  )
}
