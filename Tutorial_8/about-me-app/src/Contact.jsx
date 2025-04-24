export default function Contact({ email, github }) {
    return (
    <><h1>📧 Reach us on our Contact page.</h1><div>
        <h2>Contact Info</h2>
        <ul>
          <li>Email: {email}</li>
          <li>GitHub: {github}</li>
        </ul>
      </div></>
  );
  }