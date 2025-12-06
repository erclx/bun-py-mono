import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'

import { App } from './index'

describe('App', () => {
  it('should render the main app heading', () => {
    render(<App />)

    const heading = screen.getByRole('heading', {
      name: /my react app/i,
    })

    expect(heading).toBeInTheDocument()
  })
})
