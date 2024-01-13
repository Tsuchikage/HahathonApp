import { createBrowserRouter } from 'react-router-dom'
import Root from './routes/root'
import Auth from './routes/auth'
import MobileNavbar from './components/MobileNavbar'

export const router = createBrowserRouter([
	{
		element: <MobileNavbar />,
		children: [
			{
				path: '/',
				element: <Root />
			},
			{
				path: '/auth',
				element: <Auth />
			}
		]
	}
])
