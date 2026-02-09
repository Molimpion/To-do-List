import { CheckCircle, Circle, Trash } from 'phosphor-react';
import styles from './Task.module.css';

export interface ITask {
  id: string;
  title: string;
  isCompleted: boolean;
}

interface Props {
  task: ITask;
  onDeleteTask: (taskId: string) => void;
  onComplete: (taskId: string) => void;
}

export function Task({ task, onDeleteTask, onComplete }: Props) {
  return (
    <div className={styles.task}>
      <button 
        className={styles.checkContainer} 
        onClick={() => onComplete(task.id)}
      >
        {task.isCompleted ? (
          <CheckCircle className={styles.checkedCircle} size={24} weight="fill" />
        ) : (
          <Circle className={styles.circle} size={24} />
        )}
      </button>

      <p className={task.isCompleted ? styles.taskCompleted : ""}>
        {task.title}
      </p>

      <button 
        className={styles.deleteButton} 
        onClick={() => onDeleteTask(task.id)}
      >
        <Trash size={20} />
      </button>
    </div>
  );
}