import { PlusCircle } from 'phosphor-react';
import { useState, type ChangeEvent, type FormEvent } from 'react';
import todoLogo from '../../assets/todoLogo.svg'; 
import styles from './Header.module.css';

interface Props {
  onAddTask: (taskTitle: string) => void;
}

export function Header({ onAddTask }: Props) {
  const [title, setTitle] = useState("");

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    
    if(title.trim().length === 0) {
        return;
    }

    onAddTask(title);
    setTitle("");
  }

  function onChangeTitle(event: ChangeEvent<HTMLInputElement>) {
    setTitle(event.target.value);
  }

  return (
    <header className={styles.header}>
      <img src={todoLogo} alt="Logotipo do Todo" />

      <form className={styles.newTaskForm} onSubmit={handleSubmit}>
        <input 
          placeholder="Adicione uma nova tarefa" 
          onChange={onChangeTitle}
          value={title}
        />
        <button disabled={title.length === 0}>
          Criar 
          <PlusCircle size={20} />
        </button>
      </form>
    </header>
  );
}