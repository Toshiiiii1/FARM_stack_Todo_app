import TodoItem from './TodoItem'

export default function TodoView(props) {
    return (
        <div>
            <ul>
                {props.todoList.map(todo => <TodoItem todo={todo} deleteTodo={props.deleteTodo}/>)}
            </ul>
        </div>
    )
}
