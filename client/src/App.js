import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Form>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="formName">
              <Form.Label>Name</Form.Label>
              <Form.Control placeholder='e.g. Dog Breeds'/>
            </Form.Group>

            <Form.Group as={Col} controlId="formType">
              <Form.Label>Type</Form.Label>
              <Form.Select defaultValue="Choose...">
                <option>Choose...</option>
                <option value="1">Audio</option>
                <option value="2">Image</option>
                <option value="3">Text</option>
                <option value="4">Video</option>
              </Form.Select>
            </Form.Group>

            <Form.Group as={Col} controlId="formSize">
              <Form.Label>Size</Form.Label>
              <Form.Control placeholder='#samples per class'/>
            </Form.Group>
          </Row>

          <Row className="mb-3" controlId="formClass" >
            <Form.Label>Classes</Form.Label>
            <Form.Control type="file"/>
          </Row>


          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>        
      </header>
    </div>
  );
}

export default App;
