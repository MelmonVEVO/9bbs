import { FC, useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { BASE_URL, Post } from '../main.tsx';

// @ts-ignore
const Thread: FC = () => {
    const { boardIdx, threadIdx } = useParams()
    const [ posts, setPosts ] = useState([])

    useEffect(() => {
        axios.get(`${BASE_URL}/api/board/${boardIdx}/thread/${threadIdx}`).then((response) => {
            setPosts(response.data)
        })
    }, []);

    return (
        <div className='thread'>
            <div className='thread_heading'></div>
            <div className='posts_container'>{
                posts ? posts.map((post: Post) => (
                        <div className='post_container'>
                            <div className='post header'></div>
                            <div className='post body'>
                                {post.post_content}
                            </div>
                        </div>
                    ))
                    : <></>
            }
            </div>
        </div>
    )
}

export default Thread
