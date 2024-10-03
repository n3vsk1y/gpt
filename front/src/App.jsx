import React, { useState, useEffect } from 'react'
import './App.css'
import api from './Api'

import Header from './components/Header/Header'
import UserMessageBlock from './components/UserMessageBlock/UserMessageBlock'
import EditableUserMessageBlock from './components/EditableUserMessageBlock/EditableUserMessageBlock'
import AiMessageBlock from './components/AiMessageBlock/AiMessageBlock'

export default function App() {
	const [count, setCount] = useState(0)

	return (
		<>
			<Header />
			<main>
				<EditableUserMessageBlock />
				<AiMessageBlock />
			</main>
		</>
	)
}
