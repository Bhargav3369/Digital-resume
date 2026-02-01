import React from 'react';
import { Github, Linkedin, Mail } from 'lucide-react';
import '../styles/footer.css';

const Footer = () => {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="footer">
            <div className="footer-container">
                <div className="footer-content">
                    <div className="footer-info">
                        <h3>Madala Venkata Bhargav</h3>
                        <p>AI/ML Engineer Undergraduate</p>
                    </div>

                    <div className="footer-social">
                        <a href="https://github.com/Bhargav3369" target="_blank" rel="noopener noreferrer">
                            <Github size={24} />
                        </a>
                        <a href="https://www.linkedin.com/in/bhargav-madala" target="_blank" rel="noopener noreferrer">
                            <Linkedin size={24} />
                        </a>
                        <a href="mailto:bhargavmadala2358@gmail.com">
                            <Mail size={24} />
                        </a>
                    </div>
                </div>

                <div className="footer-bottom">
                    <p>&copy; {currentYear} Bhargav. Built with React & FastAPI.</p>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
