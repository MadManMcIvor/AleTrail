import { useState } from 'react';
import { useToken } from './LoginToken';
import LoginErrorModal from './LoginErrorModal';


function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const login = useToken()[1];
  const [modalShow, setModalShow] = useState(false);
  const [hidePassword, setHidePassword] = useState(false);


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(email, password);
    } catch (error) {
      console.log(error);
      console.log("Wrong email or password!");
      setModalShow(true);
    }
  }

  const toggleBtn = (e) => {
    e.preventDefault();
    setHidePassword(prevState => !prevState);
  }


  return (
    <>
      <LoginErrorModal
        show={modalShow}
        onHide={() => setModalShow(false)}
      />
      <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
              <div className="mb-3">
                <label htmlFor="email" className="form-label">Email</label>
                <input value={email} onChange={e => setEmail(e.target.value)} required type="email" className="form-control" id="email" placeholder="email@email.com" />
              </div>
              <div className="mb-3">
                <label htmlFor="password" className="form-label">Password</label>
                <input value={password} onChange={e => setPassword(e.target.value)} required type={hidePassword ? "text" : "password"} className="form-control" id="password" placeholder="password" />
              </div>
              <button className="btn" onClick={(e) => toggleBtn(e)}>
                {hidePassword ? "Hide password" : "View password"
                }
              </button>
              <button type="submit" className="btn btn-primary">Login</button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}


export default LoginPage;