import './Header.css'

import VersionOption from '../VersionOption'

import { versions } from '../../data/versions'
import logo from '../../assets/logo.svg'

export default function Header() {
	return (
		<header>
			<img src={logo} />
			<select>
				<VersionOption {...versions[0]} />
				<VersionOption {...versions[1]} />
				<VersionOption {...versions[2]} />
				<VersionOption {...versions[3]} />
				<VersionOption {...versions[4]} />
				<VersionOption {...versions[5]} />
				<VersionOption {...versions[6]} />
			</select>
		</header>
	)
}
