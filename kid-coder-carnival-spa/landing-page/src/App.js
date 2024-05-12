import React from 'react';
import { Navbar, Nav, Button, Container, Row, Col } from 'react-bootstrap';

function LandingPage() {
  return (
    <div>
      {/* Intro Section */}
      <header>
        <Navbar bg="dark" variant="dark" expand="lg">
          <Container>
            <Navbar.Brand href="#">Kid Coder Carnival</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="mr-auto">
                <Nav.Link href="#features">Features</Nav.Link>
                <Nav.Link href="#about">About</Nav.Link>
              </Nav>
              <Button variant="outline-light" target='_blank'  href="https://shymaaismail.tech/kids-coder-api/swagger/">Visit App</Button>
            </Navbar.Collapse>
          </Container>
        </Navbar>
        <Container>
          <Row className="justify-content-md-center">
            <Col md={8}>
              <h1>Welcome to Kid Coder Carnival</h1>
              <p>Where Young Minds Code, Compete, and Create!</p>
              <img src="cover_image.jpg" alt="Cover" className="img-fluid" />
            </Col>
          </Row>
        </Container>
      </header>

      {/* Feature Section */}
      <section id="features">
        <Container>
          <h2 className="text-center">For Kids</h2>
          <Row>
            <Col>
              <h3>Fun Challenges</h3>
              <p>Engage in exciting coding challenges tailored for kids, designed to foster creativity and problem-solving skills.</p>
            </Col>
            <Col>
              <h3>Interactive Learning</h3>
              <p>Experience interactive coding lessons and activities that make learning fun and enjoyable for young coders.</p>
            </Col>
            <Col>
              <h3>Earn Rewards</h3>
              <p>Receive badges and rewards for completing challenges and achieving milestones, encouraging continuous learning and improvement.</p>
            </Col>
          </Row>

          <h2 className="text-center mt-5">For Admins</h2>
          <Row>
            <Col>
              <h3>Manage Competitions</h3>
              <p>Create and oversee coding competitions, ensuring smooth operations and an engaging experience for participants.</p>
            </Col>
            <Col>
              <h3>Curate Challenges</h3>
              <p>Select and organize coding challenges to create diverse and stimulating competition events for young coders.</p>
            </Col>
            <Col>
              <h3>Track Progress</h3>
              <p>Monitor participant progress and performance, providing insights to enhance future competitions and learning experiences.</p>
            </Col>
          </Row>
        </Container>
      </section>

      {/* About Section */}
      <section id="about">
        <Container>
          <div>
            <h2 className="text-center">About Us</h2>
            <p>Believing in the transformative power of coding education for kids, we embarked on this journey to nurture creative and skilled minds. Our passion for empowering young learners with essential coding skills inspired the creation of Kid Coder Carnival. We're dedicated to providing a fun and engaging platform where kids can unleash their creativity, develop critical thinking abilities, and embark on a journey of lifelong learning through coding adventures.</p>
            <p>This is a Portfolio Project for ALX School Cohort 18. <a target='_blank'  href="https://www.alxafrica.com/about/">Link</a></p>
            <div>
              <h3>Full Stack Developer</h3>
              <ul className="team-member">Shymaa Mohamed Ismail</ul>
              <ul>
                <li><a target='_blank' href="https://www.linkedin.com/in/shymaa-m-ismail/">LinkedIn</a></li>
                <li><a target='_blank' href="https://github.com/ShymaaIsmail">GitHub</a></li>
              </ul>
            </div>
            <div>
              <h3>GitHub Repository</h3>
              <a target='_blank'  href="https://github.com/ShymaaIsmail/kid-coder-carnival">Link</a>
            </div>
          </div>
        </Container>
      </section>
    </div>
  );
}

export default LandingPage;
