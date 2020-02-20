import React, { useState } from "react";
import { useForm, Controller } from "react-hook-form";
import { connect } from "react-redux";
import { updateAction } from "../../../../store/index";

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
  UncontrolledDropdown,
  ButtonGroup
} from "../../../../components";

const QuestionList = props => {
  const { qu, name, listOptions } = props;
  const { final } = props;
  const [rSelected, setRSelected] = useState(null);
  const { control, handleSubmit, watch } = useForm();
  const onSubmit = data => props.updateAction(data);
  const [value, setValue] = React.useState("");

  const selectValue = watch("rSelected")
  function nextPreprocess() {
    props.saveState(props.index, { id: props.id, value });
    props.nextFn();
  }

  function previousPreprocess() {
    props.saveState(props.index, { id: props.id, value });
    props.prevFn();
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
          <ButtonGroup
            name={name}
            style={{
              marginLeft: "5px"
            }}
          >
            {listOptions.map((item, index) => (
              <Controller
                as={<Button color="primary" />}
                name={name}
                control={control}
                key={index}
                onClick={() => setRSelected(index)}
                value={item.option}
                defaultValue={item}
                active={rSelected === `${index}`}
                style={{
                  marginLeft: "5px",
                  // backgroundColor: "teal"
                }}
              >
                {item.select}
              </Controller>
            ))}
            <input type="submit" />
          </ButtonGroup>
          <p>Selected: {rSelected}</p>
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

const mapStateToProps = state => {
  return {
    bodyObject: state.bodyObject
  };
};

const mapDispatchToProps = { updateAction };

export default connect(mapStateToProps, mapDispatchToProps)(QuestionList);
