import { FC, useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import axios from 'axios';
import { BASE_URL, Thread } from '../main.tsx';

// type Props = {
// }


const BoardBrowse: FC = () => {
    const { boardIdx } = useParams()
    const [threads, setThreads] = useState([])

    useEffect(() => {
        axios.get(`${BASE_URL}/api/board/${boardIdx}`).then((response) => {
            setThreads(response.data)
        })
    }, []);



    return (<>{
        threads ? threads.map((thread: Thread) => (
            <div className='thread_container' id={`t${thread.id}`}>
                <div className='thread header'>
                    {thread.archived && <div className='tag archived'>ARCH</div> }
                    {thread.sticky && <div className='tag sticky'>STICKY</div> }
                    <span className='title'>{thread.thread_title}</span>
                    <span className='user'>{thread.op}</span>
                    <span className='date'>{thread.date_created}</span>
                    <span>
                        [<Link to={`/boards/${boardIdx}/${thread.id}`}>View</Link>]
                    </span>
                </div>
            </div>
        )) : <></>
    }</>)
}

export default BoardBrowse
