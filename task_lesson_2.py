from selene import browser, be, have


browser.open('https://duckduckgo.com/')
browser.element('[name=q]').should(be.blank).type('yashaka').press_enter()
browser.element('[id=react-layout]').should(have.text('Yashaka Mountains'))