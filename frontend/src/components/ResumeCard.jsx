import React from 'react';
import '../styles/resume-card.css';

const ResumeCard = ({ title, subtitle, date, description, items, isProminent }) => {
    // Extract Grade from description if it exists
    const gpaMatch = description?.match(/GPA:\s*([\d.]+)/i);
    const percentageMatch = description?.match(/Percentage:\s*([\d.]+%?)/i);

    const gradeLabel = gpaMatch ? 'GPA' : (percentageMatch ? 'Percentage' : null);
    const gradeValue = gpaMatch ? gpaMatch[1] : (percentageMatch ? percentageMatch[1] : null);

    return (
        <div className={`education-item ${isProminent ? 'prominent' : 'secondary'}`}>
            <div className="education-content">
                <div className="education-header">
                    <h3 className="education-degree">
                        {title}
                        {isProminent && <span className="current-badge">Current</span>}
                    </h3>
                    <div className="education-meta">
                        {date} {gradeValue && <span className="meta-separator">|</span>} {gradeValue && `${gradeLabel}: ${gradeValue}`}
                    </div>
                </div>
                <h4 className="education-institution">{subtitle}</h4>

                {isProminent && items && (
                    <ul className="education-achievements">
                        {items.split(',').map((item, index) => (
                            <li key={index}>{item.trim()}</li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
};

export default ResumeCard;
