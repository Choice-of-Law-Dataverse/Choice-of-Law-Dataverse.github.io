// script.js

const schema = {
    "users": {
        description: "Table containing user information.",
        columns: {
            "id": "Unique identifier for each user.",
            "username": "Username chosen by the user.",
            "email": "Email address of the user.",
            "created_at": "Timestamp when the user was created."
        }
    },
    "posts": {
        description: "Table containing posts created by users.",
        columns: {
            "id": "Unique identifier for each post.",
            "user_id": "Identifier of the user who created the post.",
            "title": "Title of the post.",
            "content": "Content of the post.",
            "created_at": "Timestamp when the post was created."
        },
        connections: [
            { from: "posts.user_id", to: "users.id" }
        ]
    },
    "comments": {
        description: "Table containing comments on posts.",
        columns: {
            "id": "Unique identifier for each comment.",
            "post_id": "Identifier of the post the comment belongs to.",
            "user_id": "Identifier of the user who made the comment.",
            "content": "Content of the comment.",
            "created_at": "Timestamp when the comment was created."
        },
        connections: [
            { from: "comments.post_id", to: "posts.id" },
            { from: "comments.user_id", to: "users.id" }
        ]
    }
};

function generateMermaidDiagram(schema) {
    let diagram = 'erDiagram\n';

    for (const [tableName, tableData] of Object.entries(schema)) {
        diagram += `    ${tableName} {\n`;
        for (const [columnName, columnDescription] of Object.entries(tableData.columns)) {
            diagram += `        ${columnName} ${columnName} "${columnDescription}"\n`;
        }
        diagram += `    }\n`;
    }

    for (const [tableName, tableData] of Object.entries(schema)) {
        if (tableData.connections) {
            tableData.connections.forEach(connection => {
                const [fromTable, fromColumn] = connection.from.split('.');
                const [toTable, toColumn] = connection.to.split('.');
                diagram += `    ${fromTable} ||--o| ${toTable} : "FK ${fromColumn} to ${toColumn}"\n`;
            });
        }
    }

    return diagram;
}

document.addEventListener('DOMContentLoaded', () => {
    const diagramCode = generateMermaidDiagram(schema);
    console.log(diagramCode); // Print the diagram code to console for debugging
    document.getElementById('mermaid-diagram').textContent = diagramCode;
    mermaid.init(undefined, document.querySelectorAll('.mermaid'));
});
