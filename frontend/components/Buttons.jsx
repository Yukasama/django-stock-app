import React, { Component } from 'react'

class StartButton extends Component {
    constructor(props) {
        super(props);
    }

    state = {}

    onClick = () => {
        return 0
    }

    render() {
        return (
            <div style={"color: #00ff00"} className='normal_button'>
                <i className='fa-solid fa-start'></i>
                <p>Start</p>
            </div>
        )
    }
}