import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Notice</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="student_name">Name</Label>
              <Input
                type="text"
                id="student_name"
                name="name"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter Student Name"
              />
            </FormGroup>
            <FormGroup>
              <Label for="student-majors">Majors</Label>


              <select value = {this.state.activeItem.major} onChange={this.handleChange}>
                <option value="undecided">Undecided</option>
                <option value="finance">Finance</option>
                <option value="engineering">Engineering</option>
                <option value="accounting">Accounting</option>
                <option value="marketing">Marketing</option>
                <option value="real estate">Real Estate</option>
                <option value="it">Information Technology Management</option>         
              </select>  
            </FormGroup>
            
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
