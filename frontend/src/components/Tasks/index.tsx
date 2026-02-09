import { ClipboardText } from 'phosphor-react';
import { ITask } from '../Task'; // Importamos a interface da pasta vizinha
import { Task } from '../Task';
import styles from './Tasks.module.css';

interface Props {
  tasks: ITask[];
  onDeleteTask: (taskId: string) => void;
  onComplete: (taskId: string) => void;
}

export function Tasks({ tasks, onDeleteTask, onComplete }: Props) {
  const tasksLength = tasks.length;
  const completedTasks = tasks.filter(task => task.isCompleted).length; 

  return (
    <section className={styles.tasks}>
      <header className={styles.header}>
        <div>
          <p>Tarefas criadas</p>
          <span>{tasksLength}</span>
        </div>

        <div>
          <p className={styles.textPurple}>Concluídas</p>
          <span>
            {completedTasks} de {tasksLength}
          </span>
        </div>
      </header>

      <div className={styles.listTasks}>
        {tasks.map(task => (
          <Task 
            key={task.id} 
            task={task} 
            onDeleteTask={onDeleteTask} 
            onComplete={onComplete}
          />
        ))}

        {tasks.length <= 0 && (
          <section className={styles.empty}>
            <ClipboardText size={56} />
            <div>
              <p>Você ainda não tem tarefas cadastradas</p>
              <span>Crie tarefas e organize seus itens a fazer</span>
            </div>
          </section>
        )}
      </div>
    </section>
  );
}