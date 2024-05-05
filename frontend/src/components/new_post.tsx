import { ChangeEvent, FC, FormEvent, useState } from 'react';
import axios from 'axios';

type FormData = {
    thread_id?: number
    reply_to?: number
    post_title: string
    post_contents: string
    options: string
}

type Props = {
    threadID?: number
    replyTo?: number
}


const NewPost: FC<Props> = (props: Props) => {
    const [formData, setFormData] = useState<FormData>({
        thread_id: props.threadID,
        reply_to: props.replyTo,
        post_title: '',
        post_contents: '',
        options: ''
    });

    const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target
        setFormData((previousFormData) => ({ ...previousFormData, [name]: value }))
    }

    const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault()
        axios.post('http://127.0.0.1:8000/api/posts/new', formData)
            .then((response) => {
                console.log(response)
            })
    }

    return (
        <div>
            {formData.reply_to && (
                <>
                    <p>Replying to: #{formData.reply_to}</p>
                    <button
                        onClick={() => {
                            setFormData((previousFormData) => ({ ...previousFormData, ['reply_to']: undefined }))
                        }}
                        title='Cancel'>
                        Cancel
                    </button>
                </>
            )}
            <form onSubmit={handleSubmit}>
                {!props.threadID && (
                    <>
                        <label htmlFor='post_title'>Title:</label>
                        <input name="post_title" value={formData.post_title} onChange={handleChange} />
                    </>
                )}

                <label htmlFor='post_contents'>Text:</label>
                <textarea name='post_contents' value={formData.post_contents} onChange={handleChange}/>

                <label htmlFor='options'>Options:</label>
                <input name='options' id='options' value={formData.options} onChange={handleChange} />

                <button type='submit'>Post!</button>
            </form>
        </div>
    )
}

export default NewPost
