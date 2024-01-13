import { useToggle, upperFirst } from '@mantine/hooks'
import { useForm } from '@mantine/form'
import {
	TextInput,
	PasswordInput,
	Text,
	Paper,
	Group,
	PaperProps,
	Button,
	Anchor,
	Stack
} from '@mantine/core'

import classes from './AuthForm.module.css'
import classNames from 'classnames'

const AuthForm = ({ className, ...props }: PaperProps) => {
	const [type, toggle] = useToggle(['login', 'register'])
	const form = useForm({
		initialValues: {
			username: '',
			password: ''
		},

		validate: {
			username: val =>
				val.length <= 6
					? 'Имя пользователя должно содержать не менее 6 символов'
					: null,
			password: val =>
				val.length <= 6 ? 'Пароль должен содержать не менее 6 символов' : null
		}
	})

	return (
		<Paper
			display="flex"
			p="lg"
			withBorder
			className={classNames(classes.auth, className)}
			{...props}
		>
			<Text size="lg" fw={500}>
				Добро пожаловать
			</Text>

			<form onSubmit={form.onSubmit(() => {})}>
				<Stack>
					<TextInput
						label="Имя пользователя"
						placeholder="johndoe"
						value={form.values.username}
						onChange={event =>
							form.setFieldValue('username', event.currentTarget.value)
						}
					/>
					<PasswordInput
						required
						label="Пароль"
						placeholder="Ваш пароль"
						value={form.values.password}
						onChange={event =>
							form.setFieldValue('password', event.currentTarget.value)
						}
						error={
							form.errors.password &&
							'Пароль должен содержать не менее 6 символов'
						}
					/>
				</Stack>

				<Group justify="space-between" mt="xl">
					<Anchor
						component="button"
						type="button"
						c="dimmed"
						onClick={() => toggle()}
						size="xs"
					>
						{type === 'register'
							? 'Есть аккаунт? Войти'
							: 'Нет аккаунта? Регистрация'}
					</Anchor>
					<Button type="submit">
						{upperFirst(type === 'register' ? 'Создать аккаунт' : 'Войти')}
					</Button>
				</Group>
			</form>
		</Paper>
	)
}

export default AuthForm
