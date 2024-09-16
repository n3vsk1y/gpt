import './AiMessageBlock.css'

export default function AiMessageBlock() {
	return (
		<div className="block">
			<div className="ai-block">
				<p>ai &gt;</p>
			</div>

			<div className="response-block">
				ai_response
				{/* <p>ai_response</p> */}
				{/* <p>&nbsp;</p> */}
			</div>
		</div>
	)
}
