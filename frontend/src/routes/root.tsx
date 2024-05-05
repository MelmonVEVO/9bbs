import { FC, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { Board } from '../main.tsx';
import axios from 'axios';


const Root: FC = () => {
    const [boards, setBoards] = useState<Array<Board>>([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/boards/").then((response) => {
            setBoards(response.data.results);
        })
    }, []);

    return (
        <div className="container">
            <h1>9bbs</h1>
            <div className="panel">9bbs is a message board system that lets you post interesting things and discuss them.
                Pick a board below and jump right in!
            </div>
            <div className="panel">
                {boards.map(board =>
                    <Link to={`boards/${board.board_index}/`}>{board.board_name} - /{board.board_index}/</Link>
                )}
            </div>
        </div>
    )
}

export default Root