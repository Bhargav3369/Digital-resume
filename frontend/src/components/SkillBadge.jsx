import React from 'react';
import '../styles/skill-badge.css';

const SkillBadge = ({ name, category }) => {
    return (
        <div className={`skill-badge ${category.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`}>
            {name}
        </div>
    );
};

export default SkillBadge;
