import { useState} from 'react';


function SignupForm(props){
    const [first, setFirst]= useState('');
    const [last, setLast] = useState('');
    const [email, setEmail] = useState('');
    const [username, setUsername]= useState('');
    const [password, setPassword] = useState('');


    return( 
        <>
         <div className="row">
                <div className="offset-3 col-6">
                    <div className="shadow p-4 mt-4">
                        <h1>Create Your Account</h1>
                        <form>
                            <div className="mb-3">
                                <label htmlFor="first" className="form-label">First name</label>
                                <input value = {first} onChange={ e => setFirst(e.target.value)} required type="text" className="form-control" id="first" placeholder="First name" />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="last" className="form-label">Last name</label>
                                <input value = {last} onChange={ e => setLast(e.target.value)} required type="text" className="form-control" id="last" placeholder="Last name" />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="email" className="form-label">Email</label>
                                <input value= {email} onChange={ e => setEmail(e.target.value)} required type="email" className="form-control" id="email" placeholder="email@email.com" />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="username" className="form-label">Username</label>
                                <input value = {username} onChange={ e => setUsername(e.target.value)} required type="text" className="form-control" id="username" placeholder="username" />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="password" className="form-label">Password</label>
                                <input value = {password} onChange={ e => setPassword(e.target.value)} required type="text" className="form-control" id="password" placeholder="password" />
                            </div>             
                            <button type="submit" className="btn btn-primary">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </>
    );
}

export default SignupForm; 



