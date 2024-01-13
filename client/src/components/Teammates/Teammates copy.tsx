import {
	Card,
	Grid,
	ScrollArea,
	SimpleGrid,
	Skeleton,
	Stack,
	rem
} from '@mantine/core'
import classes from './Teammates.module.css'
import classNames from 'classnames'
import { useMemo, useState } from 'react'

const PRIMARY_COL_HEIGHT = '600px'
const SECONDARY_COL_HEIGHT = `calc(${PRIMARY_COL_HEIGHT} / 4 - var(--mantine-spacing-md) / 2)`

const Teammates = () => {
	const [selected, setSelected] = useState<string | null>(null)

	const handleClick = (id: string) => {
		setSelected(id === selected ? null : id)
	}

	const items = [...Array(6).map(String)]

	const renderedItems = useMemo(() => {
		return items.map(
			(_, i) =>
				i.toString() !== selected && (
					<Grid.Col key={i} span={4} p={selected ? 0 : 8}>
						<Card
							h={SECONDARY_COL_HEIGHT}
							withBorder
							onClick={() => handleClick(i.toString())}
						>
							{i}
						</Card>
					</Grid.Col>
				)
		)
	}, [items, selected])

	return (
		<Grid className={classes.teammates} grow gutter="md">
			{selected ? (
				<>
					<Grid.Col span={8} className={classes.active}>
						<Card
							h={PRIMARY_COL_HEIGHT}
							withBorder
							onClick={() => handleClick(selected)}
						>
							{selected}
						</Card>
					</Grid.Col>
					<Grid.Col span={4}>
						<ScrollArea h={600} offsetScrollbars>
							<Stack gap="md">{renderedItems}</Stack>
						</ScrollArea>
					</Grid.Col>
				</>
			) : (
				renderedItems
			)}
		</Grid>
	)

	return (
		<Grid className={classes.teammates} grow gutter="md">
			<Grid.Col span={8} className={classes.active}>
				<Skeleton height={PRIMARY_COL_HEIGHT} radius="md" animate={false} />
			</Grid.Col>
			<Grid.Col span={4}>
				<ScrollArea h={600} offsetScrollbars>
					<Stack gap="md">
						{items.map((_, i) => (
							<Skeleton
								key={i}
								height={SECONDARY_COL_HEIGHT}
								radius="md"
								animate={false}
								className={classes.suggestion}
							/>
						))}
					</Stack>
				</ScrollArea>
			</Grid.Col>
		</Grid>
	)
}

export default Teammates
