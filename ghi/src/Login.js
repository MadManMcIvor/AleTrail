import { useAuthContext } from './LoginToken';


function Login() {
  const { token } = useAuthContext();

  // Use the token value in a fetch
  
}

const request = await fetch(url, {
    headers: { Authorization: `Bearer ${token}` },
    // Other fetch options, like method and body, if applicable
  });