import React from 'react'
import ReactDOM from 'react-dom/client'
import {
    createBrowserRouter,
    RouterProvider
} from 'react-router-dom';
import './index.css'
import Root from './routes/root.tsx';
import ErrorPage from './error-page.tsx';
import BoardBrowse from './routes/board_browse.tsx';
import Thread from './routes/thread.tsx'

export type Post = {
    'board': string,
    'poster': string | null,
    'reply_to': string | null,
    'post_title': string,
    'post_content': string,
    'post_last_modified': number
}


export type Board = {
    'board_name': string,
    'board_index': string
}

export type Thread = {
    'id': number,
    'thread_title': string,
    'board': string,
    'archived': boolean,
    'sticky': boolean,
    'date_created': number,
    'first_post_body': string,
    'op': number,
    'replies': number
}

export const BASE_URL = '127.0.0.1:5000'

const ROUTER = createBrowserRouter([
    {
        path: '/',
        element: <Root />,
        errorElement: <ErrorPage />
    },
    {
        path: 'boards/:boardIdx',
        element: <BoardBrowse />
    },
    {
        path: 'boards/:boardId/:threadId',
        element: <Thread />
    }
])


ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <RouterProvider router={ROUTER} />
    </React.StrictMode>
)
