import React, { useEffect, useState } from "react"
import { Button, Input } from 'antd'
const { Configuration, OpenAIApi } = require("openai")

const { TextArea } = Input
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
const mic = new SpeechRecognition()
const msg = new SpeechSynthesisUtterance()

mic.continuous = true
mic.interimResults = true
mic.lang = 'th-Th'

msg.lang = 'th-Th'

const configuration = new Configuration({
    apiKey: "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",
})
const openai = new OpenAIApi(configuration)

const Main = () => {
    const [isListening, setIsListening] = useState(false)
    const [note, setNote] = useState('')
    const [text, setText] = useState('')

    useEffect(() => {
        mic.onstart = () => {
            console.log('Speech recognition started')
        }

        mic.onresult = async e => {
            const transcript = Array.from(e.results)
                .map(result => result[0])
                .map(result => result.transcript)
                .join('')
            setText(transcript)

            // setText(e.target.value)
            const question = transcript
            const response = await openai.createCompletion({
                model: "text-davinci-003",
                prompt: `q: ${question}\n a: `,
                temperature: 0,
                max_tokens: 100,
                top_p: 1,
                frequency_penalty: 0.0,
                presence_penalty: 0.0,
                stop: ["\n"],
            })
            setNote(response.data.choices?.[0].text)
            // console.log(response)

        }

        msg.text = note
        window.speechSynthesis.speak(msg)

        mic.onerror = event => {
            console.error('Speech recognition error:', event.error)
        }

    }, [])

    const startListening = () => {
        setIsListening(true)
        mic.start()
    }

    const stopListening = () => {
        setIsListening(false)
        mic.stop()
    }

    return (
        <>
            <br /><br />
            <Button onClick={startListening} disabled={isListening}>
                Start Listening
            </Button>
            <Button onClick={stopListening} disabled={!isListening}>
                Stop Listening
            </Button>
            <br /><br />
            <Input type="text" id="inputText" placeholder="Questions" value={text} />
            <br /><br />
            <TextArea id="outputText" placeholder="Answers" value={note} />
            <br /><br />
        </>
    )
}

export default Main
