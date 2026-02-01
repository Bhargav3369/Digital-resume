import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { projectsAPI } from '../services/api';
import ProjectCard from '../components/ProjectCard';
import '../styles/projects.css';

const Projects = () => {
    const [projects, setProjects] = useState([]);
    const [loading, setLoading] = useState(true);
    const [filter, setFilter] = useState('All');

    useEffect(() => {
        const fetchProjects = async () => {
            try {
                const response = await projectsAPI.getProjects();
                setProjects(response.data);
            } catch (error) {
                console.error('Error fetching projects:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchProjects();
    }, []);

    const filteredProjects = filter === 'All'
        ? projects
        : projects.filter(p => p.tech_stack.includes(filter) || (filter === 'Featured' && p.featured));

    if (loading) return <div className="loading">Loading...</div>;

    return (
        <div className="projects-page">
            <h1 className="section-title">My Projects</h1>

            <div className="project-filters">
                {['All', 'Featured', 'Python', 'React.js', 'NLP', 'AI/ML'].map(f => (
                    <button
                        key={f}
                        className={`filter-btn ${filter === f ? 'active' : ''}`}
                        onClick={() => setFilter(f)}
                    >
                        {f}
                    </button>
                ))}
            </div>

            <div className="projects-grid">
                {filteredProjects.map((project, index) => (
                    <motion.div
                        key={project.id}
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: index * 0.1 }}
                    >
                        <ProjectCard {...project} />
                    </motion.div>
                ))}
            </div>

            {filteredProjects.length === 0 && (
                <p className="no-projects">No projects found for the selected filter.</p>
            )}
        </div>
    );
};

export default Projects;
