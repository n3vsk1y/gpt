import { useState } from 'react'
import './App.css'

import Header from './components/Header/Header'
import UserMessageBlock from './components/UserMessageBlock/UserMessageBlock'
import AiMessageBlock from './components/AiMessageBlock/AiMessageBlock'

export default function App() {
	const [count, setCount] = useState(0)

	return (
		<>
			<Header />
			<main>
                <UserMessageBlock />
            </main>
		</>
	)
}
