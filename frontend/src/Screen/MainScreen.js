import React from 'react'
import {useState} from 'react'
import {Form,Button,Container,Spinner} from 'react-bootstrap'
import axios from 'axios'
export default function MainScreen() {
  const [message,setMessage] = useState('')
  const [loading,setLoading] = useState(false)

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = JSON.stringify({ 'name': event.target[0].value, 'zipCode': event.target[1].value })
    console.log(data)
    try {
      setLoading(true)
      // request the backend
      const response = await axios({  
        method:"post",
        url:'http://localhost:5000/create_phrase',
        data: data,
      });
      setLoading(false)
        // console.log(response)
        setMessage(response.data.r)

    } catch(error) {
      console.log(error)
    }
  }

  return (
    <Container>
    <h1 className='py-3'>Home page</h1>
    {loading
    ?
      (
        <div>
          <Spinner animation="border" role="status">
            <span className="visually-hidden">Loading...</span>
          </Spinner>
          <h2>Hold on...</h2>
        </div>
      )
    :
    (
      <div>
      <Form onSubmit = {handleSubmit }>
        <Form.Group className="mb-3" controlId="Name">
            <Form.Control type="name" placeholder="First & Last Name" required />
        </Form.Group>

        <Form.Group className="mb-3" controlId="Zipcode">
            <Form.Control type="number" placeholder="Zip Code" required />
        </Form.Group>
        <Button variant="primary" type="submit">
            Display
        </Button>
    </Form>

    {/* display answer */}
    <h1 className='py-5'>{message}</h1>
    </div>
    )
    }
    </Container>
  )
}
