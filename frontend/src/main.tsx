import React from 'react'
import ReactDOM from 'react-dom/client'
import {
    createBrowserRouter,
    RouterProvider
} from 'react-router-dom';
import './index.css'
import Root from './routes/root.tsx';
import ErrorPage from './error-page.tsx';


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


const ROUTER = createBrowserRouter([
    {
        path: '/',
        element: <Root />,
        errorElement: <ErrorPage />
    },
    {
        path: 'boards/:boardId'
    },
    {
        path: 'boards/:boardId/:threadId'
    }
])


ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <RouterProvider router={ROUTER} />
    </React.StrictMode>
)
