import React, { useRef, useState, useEffect } from 'react'
import './EditableUserMessageBlock.css'
import checkmark from '../../assets/checkmark.svg'

export default function UserMessageBlock() {
	const editableRef = useRef(null)
	const [caretPosition, setCaretPosition] = useState({ x: 0, y: 0 })
	const [hasFocus, setHasFocus] = useState(false)

	useEffect(() => {
		const updateCaretPosition = () => {
			const selection = window.getSelection()
			if (selection.rangeCount > 0) {
				const range = selection.getRangeAt(0)
				const rect = range.getBoundingClientRect()
				setCaretPosition({
					x: rect.left + window.scrollX,
					y: rect.top + window.scrollY,
				})
			}
		}

		const editableElement = editableRef.current

		editableElement.addEventListener('keyup', updateCaretPosition)
		editableElement.addEventListener('click', updateCaretPosition)
		editableElement.addEventListener('focus', () => setHasFocus(true))
		editableElement.addEventListener('blur', () => setHasFocus(false))

		return () => {
			editableElement.removeEventListener('keyup', updateCaretPosition)
			editableElement.removeEventListener('click', updateCaretPosition)
			editableElement.removeEventListener('focus', () => setHasFocus(true))
			editableElement.removeEventListener('blur', () => setHasFocus(false))
		}
	}, [])

	const handleButtonClick = () => {
		console.log('Button clicked')
		if (editableRef.current) {
			editableRef.current.blur()
		}
	}

	return (
		<div className='block'>
			<div className='user-block'>
				<p>user &gt;</p>
			</div>

			<div
				className={`editable-block ${hasFocus ? 'focused' : ''}`}
				contentEditable='true'
                spellCheck='false'
				ref={editableRef}
				style={{
					'--caret-x': `${caretPosition.x}px`,
					'--caret-y': `calc(${caretPosition.y}px - 3px)`,
				}}
			>
				{/* <p>Привет!</p> */}
				<p>&nbsp;</p>
			</div>

			{hasFocus && (
				<button onClick={handleButtonClick}>
					<img src={checkmark} alt='Checkmark' />
				</button>
			)}
		</div>
	)
}
