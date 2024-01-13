import {
	Card,
	Grid,
	ScrollArea,
	SimpleGrid,
	Skeleton,
	Stack,
	Transition,
	rem
} from '@mantine/core'
import classes from './Teammates.module.css'
import classNames from 'classnames'
import { useEffect, useState } from 'react'
import Teammate from '../Teammate'
import TeammateThumbnail from '../TeammateThumbnail'

const Teammates = () => {
	const [mounted, setMounted] = useState(false)
	const [expandedCardIndex, setExpandedCardIndex] = useState<string | null>(
		null
	)

	const handleCardClick = (index: string) => {
		setExpandedCardIndex(prevIndex => (prevIndex === index ? null : index))
	}

	const items = [...Array(6).keys()]

	useEffect(() => {
		setMounted(true)
	}, [])

	return (
		<Transition
			mounted={mounted}
			transition="fade"
			duration={400}
			timingFunction="ease"
			keepMounted
		>
			{styles => (
				<div
					className={classNames(classes.teammates, {
						[`${classes['expanded']}`]: !!expandedCardIndex
					})}
					style={styles}
				>
					{items.map((_, i) => (
						<Card
							className={classNames(
								classes.card,
								// classes[`card-${i + 1}`],
								classes['card-img'],
								{
									[`${classes['active']}`]: expandedCardIndex === i.toString()
								}
							)}
							withBorder
							onClick={() => handleCardClick(i.toString())}
						>
							{expandedCardIndex === i.toString() ? (
								<Teammate />
							) : (
								<TeammateThumbnail />
							)}
						</Card>
					))}
				</div>
			)}
		</Transition>
	)
}

export default Teammates
