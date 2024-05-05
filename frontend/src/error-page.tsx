import { useRouteError } from 'react-router-dom';
import { FC } from 'react';


const ErrorPage: FC = () => {
    const error: unknown = useRouteError()

    return (
        <div id="error-page">
            <h1>Oops!</h1>
            <p>Sorry, an unexpected error has occurred.</p>
            <p>
                <i>
                    {
                        // @ts-expect-error I don't know.
                        error.statusText || error.message
                    }</i>
            </p>
        </div>
    )
}

export default ErrorPage
