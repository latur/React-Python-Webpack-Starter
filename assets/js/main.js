import React from 'react'
import ReactDOM from 'react-dom'

import sizes from "../scss/main.scss"
console.log('sizes: ', sizes)

ReactDOM.render(
    <div className={'react-app'}>
        Welcome!
    </div>,
    document.getElementById('app')
);

if (module.hot) module.hot.accept();