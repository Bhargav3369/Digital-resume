import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { contactAPI } from '../services/api';
import { Send, Mail, MapPin, Linkedin, Github } from 'lucide-react';
import '../styles/contact.css';

const Contact = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        subject: '',
        message: ''
    });
    const [status, setStatus] = useState({ type: '', message: '' });
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setStatus({ type: '', message: '' });

        try {
            await contactAPI.sendMessage(formData);
            setStatus({ type: 'success', message: 'Message sent successfully! I will get back to you soon.' });
            setFormData({ name: '', email: '', subject: '', message: '' });
        } catch (error) {
            const errorMsg = error.response?.data?.detail || 'Failed to send message. Please try again later.';
            setStatus({ type: 'error', message: errorMsg });
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="contact-page">
            <h1 className="section-title">Get In Touch</h1>

            <div className="contact-container">
                <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="contact-info glass-card"
                >
                    <h2>Contact Information</h2>
                    <p>Feel free to reach out for collaborations or just a friendly hello!</p>

                    <div className="info-item">
                        <Mail className="icon" />
                        <div>
                            <h3>Email</h3>
                            <p>bhargavmadala2358@gmail.com</p>
                        </div>
                    </div>

                    <div className="info-item">
                        <MapPin className="icon" />
                        <div>
                            <h3>Location</h3>
                            <p>Hyderabad, Telangana, India</p>
                        </div>
                    </div>

                    <div className="social-links">
                        <a href="https://www.linkedin.com/in/bhargav-madala" target="_blank" rel="noopener noreferrer">
                            <Linkedin />
                        </a>
                        <a href="https://github.com/Bhargav3369" target="_blank" rel="noopener noreferrer">
                            <Github />
                        </a>
                    </div>
                </motion.div>

                <motion.div
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="contact-form-container glass-card"
                >
                    <form className="contact-form" onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="name">Full Name</label>
                            <input
                                type="text"
                                id="name"
                                name="name"
                                value={formData.name}
                                onChange={handleChange}
                                required
                                placeholder="John Doe"
                            />
                        </div>

                        <div className="form-row">
                            <div className="form-group">
                                <label htmlFor="email">Email Address</label>
                                <input
                                    type="email"
                                    id="email"
                                    name="email"
                                    value={formData.email}
                                    onChange={handleChange}
                                    required
                                    placeholder="john@example.com"
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="subject">Subject</label>
                                <input
                                    type="text"
                                    id="subject"
                                    name="subject"
                                    value={formData.subject}
                                    onChange={handleChange}
                                    placeholder="Inquiry"
                                />
                            </div>
                        </div>

                        <div className="form-group">
                            <label htmlFor="message">Message</label>
                            <textarea
                                id="message"
                                name="message"
                                value={formData.message}
                                onChange={handleChange}
                                required
                                placeholder="How can I help you?"
                                rows="5"
                            ></textarea>
                        </div>

                        <button type="submit" className="btn btn-primary submit-btn" disabled={loading}>
                            {loading ? 'Sending...' : (
                                <>
                                    <Send size={18} /> Send Message
                                </>
                            )}
                        </button>

                        {status.message && (
                            <div className={`status-message ${status.type}`}>
                                {status.message}
                            </div>
                        )}
                    </form>
                </motion.div>
            </div>
        </div>
    );
};

export default Contact;
