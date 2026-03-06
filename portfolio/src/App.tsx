import './App.css'

function App() {
  return (
    <div className="container">
      <header className="header-flex">
        <div className="header-content">
          <h1 className="name">Anastasia Sersun</h1>
          <p className="title">Senior Backend Engineer → Product-Oriented Engineer</p>
          <div className="contacts">
            <span>Chișinău, Moldova</span>
            <a href="mailto:anastasya.sersun@gmail.com">anastasya.sersun@gmail.com</a>
            <a href="https://md.linkedin.com/in/anastasia-sersun" target="_blank" rel="noopener noreferrer">LinkedIn</a>
          </div>
        </div>
        <img src="/profile.png" alt="Anastasia Sersun" className="profile-pic" />
      </header>

      <section>
        <span className="section-title">Core Expertise</span>
        <div className="bento-grid">
          <div className="bento-item large">
            <h3>Backend & Architecture</h3>
            <p>10+ years of building distributed systems and event-driven architectures. Specialist in API design and complex integrations.</p>
            <div className="tech-tags">
              <span className="tag">Java</span>
              <span className="tag">Scala</span>
              <span className="tag">Spring Boot</span>
              <span className="tag">Kafka</span>
            </div>
          </div>
          <div className="bento-item medium">
            <h3>Product & Delivery</h3>
            <p>Engineering execution aligned with product goals. Collaborating with cross-functional teams for technical solution design.</p>
          </div>
          <div className="bento-item tall">
            <h3>Leadership</h3>
            <p>Mentoring developers, guiding startups, and providing technical leadership in high-impact environments.</p>
          </div>
          <div className="bento-item">
            <h3>Data Systems</h3>
            <p>NoSQL & SQL expertise: MongoDB, PostgreSQL, Elasticsearch, HBase.</p>
          </div>
          <div className="bento-item">
            <h3>Education</h3>
            <p>Master’s in Information Systems. Coursera Deep Learning certified.</p>
          </div>
        </div>
      </section>

      <section>
        <span className="section-title">Professional Experience</span>
        <div className="experience-list">
          <div className="experience-card">
            <div className="exp-header">
              <h3 className="company">Pentalog — Tripadvisor</h3>
              <span className="duration">2024 – Present</span>
            </div>
            <p className="role">Senior Backend Engineer</p>
            <ul className="contributions">
              <li>Architecting APIs for backend-driven UI in mobile clients.</li>
              <li>Translating product requirements into scalable backend capabilities.</li>
              <li>Optimizing GraphQL performance for mobile responsiveness.</li>
            </ul>
            <div className="tech-tags">
              <span className="tag">Java</span>
              <span className="tag">GraphQL</span>
              <span className="tag">BFF</span>
            </div>
          </div>

          <div className="experience-card">
            <div className="exp-header">
              <h3 className="company">Pentalog — Security Platform</h3>
              <span className="duration">2022 – 2024</span>
            </div>
            <p className="role">Backend Engineer</p>
            <ul className="contributions">
              <li>Integrated third-party compliance and security workflows.</li>
              <li>Adapted services for regulatory constraints and market shifts.</li>
              <li>Distributed system investigation and solution design.</li>
            </ul>
            <div className="tech-tags">
              <span className="tag">Java</span>
              <span className="tag">MongoDB</span>
              <span className="tag">Hibernate</span>
            </div>
          </div>

          <div className="experience-card">
            <div className="exp-header">
              <h3 className="company">Code Factory Group</h3>
              <span className="duration">2013 – 2021</span>
            </div>
            <p className="role">Backend Engineer (Java / Scala)</p>
            <ul className="contributions">
              <li>Architected microservices for international betting platforms.</li>
              <li>Led development of data platform modules (Exonar).</li>
              <li>Mentored junior developers and led team onboarding sessions.</li>
            </ul>
            <div className="tech-tags">
              <span className="tag">Scala</span>
              <span className="tag">Akka</span>
              <span className="tag">Kafka</span>
              <span className="tag">Elasticsearch</span>
            </div>
          </div>
        </div>
      </section>

      <section style={{marginTop: '8rem'}}>
        <span className="section-title">Mentorship & Ecosystem</span>
        <div className="bento-grid">
          <div className="bento-item medium">
            <h3>Startup Tracker</h3>
            <p>Cahul Digital Upgrade & Technovator. Supporting founders in refining growth strategies and measurable goals.</p>
          </div>
          <div className="bento-item medium">
            <h3>TechWomen Moldova</h3>
            <p>Java Mentor. Guiding aspiring developers through fundamentals and technical career pathing.</p>
          </div>
        </div>
      </section>

      <footer className="footer">
        <p>© 2025 Anastasia Sersun — Senior Backend Engineer</p>
        <p style={{marginTop: '0.5rem'}}>Refined with a soft dark aesthetic</p>
      </footer>
    </div>
  )
}

export default App
