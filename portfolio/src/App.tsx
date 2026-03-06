import './App.css'

function App() {
  return (
    <div className="container">
      <header className="header">
        <h1 className="name">Anastasia Sersun</h1>
        <p className="title">Senior Backend Engineer → Product-Oriented Engineer</p>
        <div className="contacts">
          <span>Chișinău, Moldova</span>
          <a href="mailto:anastasya.sersun@gmail.com">anastasya.sersun@gmail.com</a>
          <span>+373 798 82 436</span>
          <a href="https://md.linkedin.com/in/anastasia-sersun" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        </div>
      </header>

      <section>
        <span className="section-title">Core Expertise</span>
        <div className="bento-grid">
          <div className="bento-item large">
            <h3>Backend & Architecture</h3>
            <p>10+ years of building distributed systems, microservices, and event-driven architectures (Kafka). Specialist in API design and complex platform integrations.</p>
            <div className="tech-tags">
              <span className="tag">Java</span>
              <span className="tag">Scala</span>
              <span className="tag">Spring Boot</span>
              <span className="tag">Kafka</span>
            </div>
          </div>
          <div className="bento-item medium">
            <h3>Product & Delivery</h3>
            <p>Translating business requirements into robust technical solutions. Collaborating with cross-functional teams to ensure engineering execution aligns with product goals.</p>
          </div>
          <div className="bento-item tall">
            <h3>Leadership</h3>
            <p>Mentoring developers, guiding startup teams, and providing technical leadership within high-impact engineering environments.</p>
          </div>
          <div className="bento-item">
            <h3>Data Systems</h3>
            <p>Expertise in MongoDB, MySQL, PostgreSQL, Elasticsearch, and HBase.</p>
          </div>
          <div className="bento-item">
            <h3>Certifications</h3>
            <p>Neural Networks and Deep Learning — Coursera</p>
          </div>
        </div>
      </section>

      <section>
        <span className="section-title">Professional Experience</span>
        <div className="experience-list">
          <div className="experience-card">
            <div className="exp-header">
              <h3 className="company">Pentalog — Tripadvisor Platform</h3>
              <span className="duration">Apr 2024 – Present</span>
            </div>
            <p className="role">Senior Backend Engineer</p>
            <ul className="contributions">
              <li>Develop APIs providing data and UI configuration for mobile clients using backend-driven UI architecture.</li>
              <li>Optimize GraphQL queries and backend performance for mobile responsiveness.</li>
              <li>Work closely with product and mobile teams to translate requirements into backend capabilities.</li>
            </ul>
            <div className="tech-tags">
              <span className="tag">Java</span>
              <span className="tag">GraphQL</span>
            </div>
          </div>

          <div className="experience-card">
            <div className="exp-header">
              <h3 className="company">Pentalog — Security Platform</h3>
              <span className="duration">Jul 2022 – Apr 2024</span>
            </div>
            <p className="role">Backend Engineer</p>
            <ul className="contributions">
              <li>Integrated third-party platforms while preserving existing business workflows.</li>
              <li>Adapted backend services for new market requirements and regulatory constraints.</li>
              <li>Investigated complex issues across distributed services.</li>
            </ul>
            <div className="tech-tags">
              <span className="tag">Java</span>
              <span className="tag">MongoDB</span>
              <span className="tag">MySQL</span>
              <span className="tag">Hibernate</span>
            </div>
          </div>

          <div className="experience-card">
            <div className="exp-header">
              <h3 className="company">Pentalog — StraighterLine (EdTech)</h3>
              <span className="duration">Feb 2021 – Jul 2022</span>
            </div>
            <p className="role">Backend Engineer</p>
            <ul className="contributions">
              <li>Developed microservices for course enrollment and progress tracking.</li>
              <li>Implemented event-driven communication using Kafka.</li>
            </ul>
            <div className="tech-tags">
              <span className="tag">Java</span>
              <span className="tag">Spring Boot</span>
              <span className="tag">Kafka</span>
            </div>
          </div>

          <div className="experience-card">
            <div className="exp-header">
              <h3 className="company">Code Factory Group</h3>
              <span className="duration">2013 – 2021</span>
            </div>
            <p className="role">Backend Engineer (Java / Scala)</p>
            <ul className="contributions">
              <li>Developed multi-tenant betting platforms and trade systems.</li>
              <li>Architected microservices platforms using Scala and Akka.</li>
              <li>Led development of modules within the Exonar data platform.</li>
              <li>Mentored junior developers and supported team onboarding.</li>
            </ul>
            <div className="tech-tags">
              <span className="tag">Java</span>
              <span className="tag">Scala</span>
              <span className="tag">Akka</span>
              <span className="tag">RabbitMQ</span>
              <span className="tag">Elasticsearch</span>
            </div>
          </div>
        </div>
      </section>

      <section style={{marginTop: '6rem'}}>
        <span className="section-title">Ecosystem & Mentorship</span>
        <div className="bento-grid">
          <div className="bento-item medium">
            <h3>Startup Tracker</h3>
            <p>Cahul Digital Upgrade & Technovator. Helped founders identify growth challenges and define measurable milestones.</p>
          </div>
          <div className="bento-item medium">
            <h3>TechWomen Moldova</h3>
            <p>Java Mentor (2021–2024). Conducted weekly sessions on fundamentals and career planning for aspiring developers.</p>
          </div>
        </div>
      </section>

      <footer className="footer">
        <p>© 2025 Anastasia Sersun — Senior Backend Engineer</p>
        <p style={{marginTop: '0.5rem', opacity: 0.5}}>Built with React & Vanilla CSS</p>
      </footer>
    </div>
  )
}

export default App
