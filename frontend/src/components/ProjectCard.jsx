import React, { useState } from 'react';
import { Github, ExternalLink, ChevronDown, ChevronUp } from 'lucide-react';
import '../styles/project-card.css';

const ProjectCard = ({ title, description, tech_stack, github_url, live_url, image_url }) => {
    const [isExpanded, setIsExpanded] = useState(false);

    // Threshold for showing "Read More"
    const isLongDescription = description.length > 150;
    const displayDescription = isExpanded ? description : (isLongDescription ? `${description.substring(0, 150)}...` : description);

    return (
        <div className={`project-card glass-card ${isExpanded ? 'expanded' : ''}`}>
            <div className="project-image">
                {image_url ? (
                    <img src={image_url} alt={title} />
                ) : (
                    <div className="project-image-placeholder">
                        <span>{title.charAt(0)}</span>
                    </div>
                )}
            </div>

            <div className="project-info">
                <h3 className="project-title">{title}</h3>

                <div className="project-description-container">
                    <p className="project-description">{displayDescription}</p>
                    {isLongDescription && (
                        <button
                            className="read-more-btn"
                            onClick={(e) => {
                                e.stopPropagation();
                                setIsExpanded(!isExpanded);
                            }}
                        >
                            {isExpanded ? (
                                <>Show Less <ChevronUp size={14} /></>
                            ) : (
                                <>Read More <ChevronDown size={14} /></>
                            )}
                        </button>
                    )}
                </div>

                <div className="project-tech">
                    {tech_stack.split(',').map((tech, index) => (
                        <span key={index} className="tech-tag">{tech.trim()}</span>
                    ))}
                </div>

                <div className="project-links">
                    {github_url && (
                        <a href={github_url} target="_blank" rel="noopener noreferrer" className="project-link">
                            <Github size={18} /> Code
                        </a>
                    )}
                    {live_url && (
                        <a href={live_url} target="_blank" rel="noopener noreferrer" className="project-link">
                            <ExternalLink size={18} /> Demo
                        </a>
                    )}
                </div>
            </div>
        </div>
    );
};

export default ProjectCard;
