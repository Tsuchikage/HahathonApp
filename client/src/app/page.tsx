'use client'
import {
	createEffect,
	createGate,
	useGate,
	useUnit,
	restore,
	sample
} from '../lib/state-engine'

type Info = {
	app_name: string
	environment: string
}

const fetchInfoFx = createEffect<void, Info>(async () => {
	const url = `/api/common/info`
	const req = await fetch(url)
	return req.json()
})

const $info = restore(fetchInfoFx.doneData, null)

const HomeGate = createGate()

sample({
	source: HomeGate.open,
	target: fetchInfoFx
})

const Loading = () => <div>I am loading huh?</div>

export default function Home() {
	useGate(HomeGate)
	const loading = useUnit(fetchInfoFx.pending)
	const info = useUnit($info)

	return (
		<main>
			<h1>HOME</h1>
			{loading ? (
				<Loading />
			) : (
				<div>
					<pre>{JSON.stringify(info, null, 2)}</pre>
				</div>
			)}
		</main>
	)
}
