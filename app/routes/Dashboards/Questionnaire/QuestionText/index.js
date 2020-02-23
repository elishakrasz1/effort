import React, { useState } from "react";
import { useForm, Controller } from "react-hook-form";
import { connect } from 'react-redux'
import { updateAction } from '../../../../store/index'
import _ from "lodash";

import {
  Container,
  Wizard,
  Card,
  Nav,
  NavItem,
  NavLink,
  CardFooter,
  CardBody,
  Button,
  Row,
  Col,
  Table,
  Form,
  FormGroup,
  Input,
  InputGroup,
  InputGroupAddon,
  Label,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  UncontrolledDropdown
} from "../../../../components";

const QuestionText = props => {
  const { qu, name } = props;
  const { final } = props;
  const { control, handleSubmit } = useForm();
  const onSubmit = (data) => props.updateAction(data)

  function nextPreprocess() {
    props.saveState(props.index, { id: props.id });
    // props.saveState(props.index, { id: props.id, value });
    props.nextFn();
  }

  function previousPreprocess() {
    props.saveState(props.index, { id: props.id });
    // props.saveState(props.index, { id: props.id, value });
    props.prevFn();
  }
  function onValueChange(newValue) {
    if (value === newValue) {
      setValue(newValue);
      return;
    }
    setValue(newValue);
    console.log('new', newValue)
  }
  return (
    <div>
      <CardBody
        style={{
          height: "20vh",
          marginLeft: "100px"
        }}
      >
        <h1>{qu}</h1>
      </CardBody>
      <CardBody
        style={{
          height: "20vh",
          marginLeft: "100px"
        }}
      >
        <Form onSubmit={handleSubmit(onSubmit)}>
          <FormGroup>
            <Label style={{
                marginLeft: '18px'
            }}>Please Enter..</Label>
            <Col sm={3}>
              <Controller as={<Input />} type="text" name={name} control={control} defaultValue="" />
              <input type="submit" />
            </Col>
          </FormGroup>
        </Form>
      </CardBody>
      <CardFooter className="p-4 bt-0">
        <div className="d-flex">
          <Button onClick={previousPreprocess} color="primary" className="mr-3">
            <i className="fa fa-angle-left mr-2"></i>
            Previous
          </Button>
          <Button
            onClick={nextPreprocess}
            color="primary"
            className="ml-auto px-4"
          >
           {final ? "Finish" : "Next"}
            <i className="fa fa-angle-right ml-2"></i>
          </Button>
        </div>
      </CardFooter>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    bodyObject: state.bodyObject
  }
}

const mapDispatchToProps = { updateAction}


export default connect(mapStateToProps, mapDispatchToProps)(QuestionText)
