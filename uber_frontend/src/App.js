import React from 'react';
import logo from './logo.svg';
import './App.css';

function Cell(props){
    return <div> Cell 123</div>
}

function Board(props){
    const {n, user_one, user_two} = props;

    const generate_data = (n) => {
        let data = [];
        for (let i=0; i<n; i++){
            for (let j=0; j<n; j++){
                data[i][j] = `${i}x${j}`;
                }
            }
            return data;
    };

    const render_cells = (data) => {
        return data.map(cell => <Row cells={cells})
    }

    const cells = render_cells();

    return (
        <div style={{
            background:"#EEE",
            margin: 100
        }}>
            {cells}
        </div>
    )
}

function App() {

  return (
    <div>
        <Board n={5}/>
    </div>
  );
}

export default App;
